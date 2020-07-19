from builtins import range
from builtins import object
import numpy as np


class TwoLayerNet(object):
    """
    A two-layer fully-connected neural network with ReLU nonlinearity and
    softmax loss that uses a modular layer design. We assume an input dimension
    of D,a hidden dimension of H,and perform classification over C classes.
    """

    def __init__(
        self,
        input_dim=3*32*32,
        hidden_dim=100,
        num_classes=10,
        weight_scale=1e-3,
        reg=0.0,
    ):
        self.params={}
        self.reg=reg

        self.params["W1"]=np.random.randn(input_dim,hidden_dim)*weight_scale
        self.params["W2"]=np.random.randn(hidden_dim,num_classes)*weight_scale
        self.params["b1"]=np.zeros(hidden_dim)
        self.params["b2"]=np.zeros(num_classes)

    def loss(self,X,y=None):

        scores=None

        mid,cache1=affine_relu_forward(X,self.params["W1"],self.params["b1"])
        out,cache2=affine_forward(mid,self.params["W2"],self.params["b2"])
        scores=out

        # If y is None then we are in test mode so just return scores
        if y is None:
            return scores

        loss,grads=0,{}

        loss,dout=softmax_loss(scores,y)
        loss += 0.5*self.reg*(np.sum(self.params["W1"]**2))+0.5*self.reg*(
            np.sum(self.params["W2"]**2)
        )

        dout,grads["W2"],grads["b2"]=affine_backward(dout,cache2)
        _,grads["W1"],grads["b1"]=affine_relu_backward(dout,cache1)

        grads["W2"] += self.reg*self.params["W2"]
        grads["W1"] += self.reg*self.params["W1"]

        return loss,grads


class FullyConnectedNet(object):
    """
    A fully-connected neural network with an arbitrary number of hidden layers,
    ReLU nonlinearities,and a softmax loss function. This will also implement
    dropout and batch/layer normalization as options.
    """

    def __init__(
        self,
        hidden_dims,
        input_dim=3*32*32,
        num_classes=10,
        dropout=1,
        normalization=None,
        reg=0.0,
        weight_scale=1e-2,
        dtype=np.float32,
        seed=None,
    ):

        self.normalization=normalization
        self.use_dropout=dropout != 1
        self.reg=reg
        self.num_layers=1+len(hidden_dims)
        self.dtype=dtype
        self.params={}

        dims=np.hstack((input_dim,hidden_dims,num_classes))
        
        for i in range(self.num_layers):
            self.params["W%d"%(i+1)]=weight_scale*np.random.randn(dims[i],dims[i+1])
            self.params["b%d"%(i+1)]=np.zeros(dims[i+1])

        if self.normalization is not None:
            for i in range(len(hidden_dims)):
                self.params["gamma"+str("%d"%(i+1))]=np.ones(dims[i+1])
                self.params["beta"+str("%d"%(i+1))]=np.zeros(dims[i+1])

        self.dropout_param={}
        if self.use_dropout:

            self.dropout_param={"mode": "train","p": dropout}
            if seed is not None:
                self.dropout_param["seed"]=seed

        self.bn_params=[]
        if self.normalization=="batchnorm":
            self.bn_params=[{"mode": "train"} for i in range(self.num_layers - 1)]

        if self.normalization=="layernorm":
            self.bn_params=[{} for i in range(self.num_layers - 1)]

        # Cast all parameters to the correct datatype
        for k,v in self.params.items():
            self.params[k]=v.astype(dtype)

    def loss(self,X,y=None):
        """
        Compute loss and gradient for the fully-connected net.
        """
        X=X.astype(self.dtype)
        mode="test" if y is None else "train"

        # Set train/test mode for batchnorm params and dropout param since they
        # behave differently during training and testing.
        if self.use_dropout:
            self.dropout_param["mode"]=mode
        if self.normalization=="batchnorm":
            for bn_param in self.bn_params:
                bn_param["mode"]=mode
        scores=None

        XX=X.reshape(X.shape[0],-1).copy()
        N,D=XX.shape

        # the params between input layer and first hidden layer
        hidden_mid_value=[]
        hidden_out_value=[]

        cache_af_value=[]
        cache_relu_value=[]
        cache_bn_value=[]
        cache_ln_value=[]
        cache_dropout_value=[]

        hidden_out=X

        # the forward pass between input layer/hidden layer and hidden layer
        num_hidden_layers=self.num_layers - 1
        for i in range(num_hidden_layers):

            str_W="W"+str("%d"%(i+1))
            str_b="b"+str("%d"%(i+1))
            str_gamma="gamma"+str("%d"%(i+1))
            str_beta="beta"+str("%d"%(i+1))

            hidden_in,cache_af=affine_forward(
                hidden_out,self.params[str_W],self.params[str_b]
            )
            cache_af_value.append(cache_af)

            if self.normalization=="batchnorm":
                hidden_norm,cache_bn=batchnorm_forward(
                    hidden_in,
                    self.params[str_gamma],
                    self.params[str_beta],
                    self.bn_params[i],
                )  # do not forget gamma & beta
                cache_bn_value.append(cache_bn)

            elif self.normalization=="layernorm":
                hidden_norm,cache_ln=layernorm_forward(
                    hidden_in,
                    self.params[str_gamma],
                    self.params[str_beta],
                    self.bn_params[i],
                )
                cache_ln_value.append(cache_ln)
            else:
                hidden_norm=hidden_in

            hidden_mid,cache_relu=relu_forward(hidden_norm)
            hidden_mid_value.append(hidden_mid)
            cache_relu_value.append(cache_relu)

            if self.use_dropout:
                hidden_out,cache_dropout=dropout_forward(hidden_mid,self.dropout_param)
                cache_dropout_value.append(cache_dropout)
            else:
                hidden_out=hidden_mid

            hidden_out_value.append(hidden_out)  # recorde forward pass value for backprop

        # the params between last hidden layer and output layer,no gamma and beta
        str_W="W"+str("%d"%(num_hidden_layers+1))
        str_b="b"+str("%d"%(num_hidden_layers+1))

        scores=hidden_out.dot(self.params[str_W])+self.params[str_b]

        # If test mode return early
        if mode=="test":
            return scores

        loss,grads=0.0,{}
        data_loss,dscores=softmax_loss(scores,y)
        reg_loss=0.0
        for i in range(self.num_layers):
            str_W="W"+str("%d"%(i+1))
            reg_loss += np.sum(self.params[str_W]**2)
        reg_loss=0.5*self.reg*reg_loss
        loss=data_loss+reg_loss
        str_W="W"+str("%d"%self.num_layers)
        str_b="b"+str("%d"%self.num_layers)
        grads[str_W]=np.dot(hidden_out.T,dscores)+self.reg*self.params[str_W]
        grads[str_b]=np.sum(dscores,axis=0)
        grad_x_in=np.dot(dscores,self.params[str_W].T)

        for i in range(num_hidden_layers,0,-1):
            if self.use_dropout:
                grad_x_mid=dropout_backward(grad_x_in,cache_dropout_value[i - 1])
            else:
                grad_x_mid=grad_x_in
            # Pass ReLU
            grad_x_norm=relu_backward(grad_x_mid,cache_relu_value[i - 1])
            str_gamma="gamma"+str("%d"%i)
            str_beta="beta"+str("%d"%i)
            if self.normalization is not None:
                if self.normalization=="batchnorm":
                    grad_x_out,grads[str_gamma],grads[str_beta]=batchnorm_backward_alt(grad_x_norm,cache_bn_value[i - 1])  # Do not forget dgamma,dbeta
                if self.normalization=="layernorm":
                    grad_x_out,grads[str_gamma],grads[str_beta]=layernorm_backward(grad_x_norm,cache_ln_value[i - 1])
            else:
                grad_x_out=grad_x_norm

            str_W="W"+str("%d"%i)
            str_b="b"+str("%d"%i)
            grad_x_in,grads[str_W],grads[str_b]=affine_backward(grad_x_out,cache_af_value[i - 1])
            grads[str_W] += self.reg*self.params[str_W]
        return loss,grads


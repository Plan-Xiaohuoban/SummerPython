df2 = pd.DataFrame(
    {
        "A": 1,
        "B": pd.Timestamp("20200718"),
        "C": pd.Series(1, index=list(range(4), dtype="float32")),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)


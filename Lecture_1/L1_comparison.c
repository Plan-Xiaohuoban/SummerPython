char *reverseLeftWords(char *s, int n)
{
    int len = strlen(s), k = 0;
    char *res = malloc((len + 1) * sizeof(char));
    char *p = s + n;
    for (int i = 0; i < len - n; i++)
    {
        res[k++] = p[i];
    }
    for (int i = 0; i < n; i++)
    {
        res[k++] = s[i];
    }
    res[k] = '\0';
    return res;
}



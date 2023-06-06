function minLength(s: string): number {
    while (s.includes('AB') || s.includes('CD')) {
        s = s.replace(/AB|CD/, '');
    }

    return s.length
};
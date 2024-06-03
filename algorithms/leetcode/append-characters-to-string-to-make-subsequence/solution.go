func appendCharacters(s string, t string) int {
	f, longest := 0, 0

	for f < len(s) && longest < len(t) {
		if s[f] == t[longest] {
			longest++
		}
		f++
	}

	return len(t) - longest
}
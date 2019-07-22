class BooleanSearch():
    def __init__(self, term1_postings, term2_postings):
        self.and_matches = self.and_search(term1_postings, term2_postings)
        self.or_matches = self.or_search(term1_postings, term2_postings)
        self.not_matches = self.not_search(term1_postings, term2_postings)

    def and_search(self, term1_postings, term2_postings):
        term1_iter = iter(term1_postings)
        term2_iter = iter(term2_postings)
        term1_doc = term1_postings.__next__()
        term2_doc = term2_postings.__next__()

        matches = []
        while term1_doc != None and term2_doc != None:
            if term1_doc == term2_doc:
                matches.append(term1_doc)
            elif term1_doc < term2_doc:
                term1_doc = term1_iter.__next__()
            else:
                term2_doc = term2_iter.__next__()
        return matches

    def or_search(self, term1_postings, term2_postings):
        """Get union of all documents in both lists"""
        term1_iter = iter(term1_postings)
        term2_iter = iter(term2_postings)
        term1_doc = term1_iter.__next__()
        term2_doc = term2_iter.__next__()

        # Get matches in term1_doc
        matches = []
        while term1_doc != None or term2_doc != None:
            if term1_doc == term2_doc:
                matches.append(term1_doc)
            elif term1_doc < term2_doc:
                term1_doc = term1_postings.__next__()
            else:
                term2_doc = term2_postings.__next__()
        return matches

    def not_search(self, term1_postings, term2_postings):
        """Get document IDs in between and_search matches.
        """
        matches = []
        return matches
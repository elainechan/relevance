class BooleanSearch:
    def __init__(self, term1_postings, term2_postings):
        self.and_matches = self.and_search(term1_postings, term2_postings)
        self.or_matches = self.or_search(term1_postings, term2_postings)
        self.not_matches = self.not_search(term1_postings, term2_postings)

    def and_search(self, term1_postings, term2_postings):
        term1_doc = term1_postings.next()
        term2_doc = term2_postings.next()

        matches = []
        while term1_doc != None and term2_doc != None:
            if term1_doc == term2_doc:
                matches.append(term1_doc)
            elif term1_doc < term2_doc:
                term1_doc = term1_postings.next()
            else:
                term2_doc = term2_postings.next()
        return matches

    def or_search(self, term1_postings, term2_postings):
        """Get union of all documents in both lists"""
        term1_doc = term1_postings.next()
        term2_doc = term2_postings.next()

        # Get matches in term1_doc
        matches = []
        while term1_doc != None or term2_doc != None:
            if term1_doc == term2_doc:
                matches.append(term1_doc)
            elif term1_doc < term2_doc:
                term1_doc = term1_postings.next()
            else:
                term2_doc = term2_postings.next()
        return matches

    def not_search(self):
        """Get document IDs in between and_search matches.
        """
        matches = []
        return matches


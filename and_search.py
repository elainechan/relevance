def and(term1_postings, term2_postings):
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

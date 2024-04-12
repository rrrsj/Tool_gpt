import arxiv

def get_arxiv_paper(query):
    client = arxiv.Client()
    result = arxiv.Search\
    (
        query = query,
        max_results = 3,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )
    ans=''
    for result in client.results(result):
        ans=ans+result.entry_id+'  ->   '+result.title+'\n'
    return ans
print(get_arxiv_paper('Mamba'))
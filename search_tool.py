import sys

query = input("Enter your query: ").strip()

documents = [
    "Python is a programming language",
    "Java is used for software development",
    "Machine learning uses data to learn patterns",
    "Python is popular for artificial intelligence"
]

def search_tool(query):
    if isinstance(query, str):
        pass
    elif query is None:
        return "query cant be None"
    else:
        return "query isnt a string"
    if not query.strip():
        return "query can't be just spaces or empty."

    try:
        chk = float(query)
        return "query cant be an integer or float or negative integer."
    except ValueError:
        pass
    fail_query=["query cant be None", "query can't be just spaces or empty.", "query cant be an integer or float or negative integer."]

    if query not in fail_query:
        return query
    else:
        print(query)
        print("Encountered an issue in query to prevent crash creating a manual query")
        query = "i am fallback query"
    
    return query

prc_query = search_tool(query)

def search(prc_query):
    if prc_query == "i am fallback query":
        print("Due to query invalid stopping program")
        sys.exit()
    else:
        prc_query = prc_query.lower()
    rel_doc =[]
    for doc in documents:
        doc = doc.lower()
        if prc_query in doc:
            rel_doc.append(doc)
    return rel_doc

result = search(prc_query)
print(result)
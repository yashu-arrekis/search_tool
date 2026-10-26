query = input("Enter your query: ").strip()

def search_tool(query):
    if isinstance(query, str):
        pass
    if query is None:
        print("query cant be None")
        return "query is unsupported"
    try:
        chk = int(query)
        return "query cant be an integer."
    except ValueError:
        pass
    
    if not query.strip():
        print("query can't be just spaces or empty.")
        return "query is unsupported"
    else:
        return query

print(search_tool(query))

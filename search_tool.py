query = input("Enter your query: ").strip()

def search_tool(query):
    try:
        int(query)
        print("query cant be an integer.")
    except ValueError:
        return query
    if query is None:
        print("query cant be None")
        return "query is unsupported"
    elif not query.strip():
        print("query can't be just spaces or empty.")
        return "query is unsupported"
    else:
        return query

print(search_tool(query).strip())
def preprocess(visitors):
    cumulative_sums = [0] * (len(visitors) + 1)
    for i in range(1, len(visitors) + 1):
        cumulative_sums[i] = cumulative_sums[i - 1] + visitors[i - 1]
    return cumulative_sums

def answer_queries(cumulative_sums, queries):
    results = []
    for query in queries:
        start, end = query
        if start < 0 or end >= len(cumulative_sums) - 1:
            results.append(0)
        else:
            total_visitors = cumulative_sums[end + 1] - cumulative_sums[start]
            results.append(total_visitors)
    return results

def main():
    try:
        visitors_input = input()
        visitors = list(map(int, visitors_input.split()))
        cumulative_sums = preprocess(visitors)
        num_queries = int(input())
        queries = []
        for _ in range(num_queries):
            query_input = input()
            query = tuple(map(int, query_input.split()))
            queries.append(query)
        output = answer_queries(cumulative_sums, queries)
        for result in output:
            print(result)
    except ValueError:
        print("Input is not in correct format or missing")

main()
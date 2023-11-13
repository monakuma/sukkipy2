scores={'network':60,'database':80,'security':55}
# del scores['security']

# scores=scores.pop('network')
# print(scores)
total=sum(scores.values())
print(list(scores.keys()))
print(scores.values())
print(total)
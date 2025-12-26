def min_max(lst):
  new_list= []
  new_list.append(min(lst))
  new_list.append(max(lst))
  return new_list


print(min_max([1,2,3,4,5]))
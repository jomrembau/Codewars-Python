def get_size(w,h,d):
   size_list = []
   size_list.append(2 * ((w*h)+(w*d)+(h*d)))
   size_list.append(w*h*d)
   return size_list

print(get_size(4,2,6))
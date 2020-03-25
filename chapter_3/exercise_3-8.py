bucket_list = ['Sweeden', 'Russia', 'France', 'Italy', 'England', 'Germany']

print(f"Original list order: {bucket_list}")
print(f"Displayed in sorted order: {sorted(bucket_list)}")  # display sorted
print(f"Original list order: {bucket_list}")

print(f"\nDisplayed in reverse sorted order: "
      f"{sorted(bucket_list, reverse=True)}")   # display reverse sorted
print(f"Original list order: {bucket_list}")

bucket_list.reverse()         # actually reverse the order
print(f"\nList order now reversed: {bucket_list}")

bucket_list.reverse()         # do it again and it is back the way it was
# display reverse # sorted
print(f"\nReverse back to original order: {bucket_list}")

bucket_list.sort()	# permanently sort the list
print(f"\nPermanently sorted list: {bucket_list}")    # display permanently sorted list

bucket_list.sort(reverse=True)	# permanently reverse sort the list
print(f"\nPermanently reversed sorted list: {bucket_list}") # display permanently reverse sorted list

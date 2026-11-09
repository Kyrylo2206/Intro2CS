plan = ["going to university", "reading books", "doing sports", "eating meals", "playing games"]
print(plan[0])
print(plan[4])
print(plan[1:4])
print(plan[::-1])
plan[1] = "sleeping"
print(plan)
plan.insert(0, "going to the shop")
plan.append("doing homework")
plan.remove("eating meals")
weekend = ["walking", "relaxing"]
plan.extend(weekend)
print(plan)
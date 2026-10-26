slices_per_student = 3
students = 14
present_students = 10
total_slices_needed = slices_per_student * present_students
cost_per_slice = 500 /present_students
boxes_to_order = total_slices_needed // 8
leftover_slices = (boxes_to_order*8) % present_students

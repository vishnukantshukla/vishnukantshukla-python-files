length_of_rectangle_in_feet=eval(input("Enter the length of the rectangular floor : "))
breadth_of_the_rectangle_in_feet=eval(input("Enter the breadth of the the rectangular floor : "))
length_of_the_tiles_in_inches=eval(input("Enter the length of the tiles: "))
breadth_of_the_tiles_in_inches=eval(input("Enter the breadth of the tiles : "))
Total_area_of_rectangular_floor_in_square_feet=(length_of_rectangle_in_feet*breadth_of_the_rectangle_in_feet)
Total_area_of_one_tile_in_square_feet=(length_of_the_tiles_in_inches*breadth_of_the_tiles_in_inches)/144
total_number_of_tiles_required=Total_area_of_rectangular_floor_in_square_feet/Total_area_of_one_tile_in_square_feet
Number_of_set_of_10_tiles_required=total_number_of_tiles_required/10
print(" The total number of tiles required is = ",total_number_of_tiles_required)
print("The total number of sets of 10 tiles required = ",Number_of_set_of_10_tiles_required)




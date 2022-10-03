import arcade

arcade.open_window(1000, 800, "Build a house")
arcade.set_background_color(arcade.color.BABY_BLUE)

arcade.start_render()
# Code for floor
arcade.draw_lrtb_rectangle_filled(0, 1000, 200, 0, arcade.color.GREEN)
# Code for house structure
arcade.draw_xywh_rectangle_filled(340, 150, 350, 250, arcade.color.BEIGE)
# Code for Chimney
arcade.draw_xywh_rectangle_filled(340, 400, 50, 120, arcade.color.BRICK_RED)
# Code for roof
arcade.draw_triangle_filled(340, 400, 692, 400, 516, 600,  arcade.color.BROWN)
# Code for door
arcade.draw_xywh_rectangle_filled(570, 150, 70, 120, arcade.color.BROWN)
arcade.draw_xywh_rectangle_outline(570, 150, 70, 120, arcade.color.BLACK)
# Code for door knob
arcade.draw_circle_filled(620, 200, 5, arcade.color.GOLD)
# Code for window
arcade.draw_xywh_rectangle_filled(390, 270, 70, 70, arcade.color.GRAY_BLUE)
arcade.draw_xywh_rectangle_outline(390, 270, 70, 70, arcade.color.BLACK)
# window panels
arcade.finish_render()
arcade.run()

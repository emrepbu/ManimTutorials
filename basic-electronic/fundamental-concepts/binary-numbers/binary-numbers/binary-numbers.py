from manim import *

class DigitalSignalGraph(Scene):
    def construct(self):
        # Digital signal data
        data = [0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0]
        
        # Digital signal lines
        points = [Line(start=[0, 0, 0], end=[0, data[0], 0])]  # Start the first point from the origin
        for i in range(1, len(data)):
            points.append(Line(start=[i - 1, data[i - 1], 0], end=[i, data[i - 1], 0]))
            if data[i] != data[i - 1]:  # Add vertical line for high-low changes
                points.append(Line(start=[i, data[i - 1], 0], end=[i, data[i], 0]))
        points.append(Line(start=[len(data) - 1, data[-1], 0], end=[len(data), data[-1], 0]))  # Last horizontal line

        # Coordinate axes
        axes = Axes(
            x_range=[0, len(data)], 
            y_range=[0, 5],  
            axis_config={"include_numbers": True},
        ).move_to(RIGHT * 0.5 + UP * 0.5)

        x_label = axes.get_x_axis_label("t \\text{ (time)}", edge=DOWN, direction=DOWN, buff=1.3).to_corner(DR)
        y_label = axes.get_y_axis_label("\\text{bit}", edge=DOWN, direction=DOWN, buff=0.5).to_corner(UL)

        # Title text
        title = Text("Digital Signal Graph", font_size=64).move_to(ORIGIN)

        # Group the signal lines and rectangles
        signal = VGroup(*points).move_to(RIGHT * 0.25 + DOWN * 1.5)

        shaded_areas = VGroup()  # Group to hold shaded areas
        text_objects = VGroup()  # Group to hold text objects
        rects = []

        # Create rectangles and add text for each signal data point
        for i, val in enumerate(data):
            rect = Rectangle(
                width=1,  
                height=val,  
                color=BLUE, 
                fill_opacity=0.3,  
                stroke_width=0  
            ).shift(RIGHT * i + DOWN * val / 2)  # Align each area with the correct point on the x-axis

            if val == 1:
                shaded_areas.add(rect)
                rects.append(rect)
                text = Text(str(val), font_size=24).move_to(rect.get_center())  # Place text in the center of the rectangle
                text_objects.add(text)
            else:
                text = Text(str(val), font_size=24, color=WHITE).move_to(RIGHT * i + DOWN * 0.5)  # Place text below for 0
                text_objects.add(text)

        # Check edges and add lines to touching edges
        for i in range(len(rects) - 1):
            if abs(rects[i].get_center()[0] - rects[i + 1].get_center()[0]) < 1.1:
                rects[i].set_stroke(width=1, color=WHITE)
                rects[i + 1].set_stroke(width=1, color=WHITE)

        shaded_areas.move_to(RIGHT * 0.25 + DOWN * 1.5)
        text_objects.move_to(RIGHT * 0.25 + DOWN * 1.5)
        
        # Animation sequence
        # 1. Add title text and scale it to move to the top-right corner
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.scale(0.5).to_corner(UR))
        self.wait(1)

        # 2. Create coordinate system
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(1)

        # 3. Animate the rectangles with "grow in"
        self.play(LaggedStartMap(GrowFromCenter, shaded_areas, lag_ratio=0.1), Create(signal))
        self.wait(2)

        # 4. Add text objects
        self.play(LaggedStartMap(Write, text_objects, lag_ratio=0.1))
        self.wait(2)

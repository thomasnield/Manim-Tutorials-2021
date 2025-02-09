from manim import *
import numpy as np
import random


class Tute1(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-7, 7, 1], y_range=[-4, 4, 1]).add_coordinates()
        box = Rectangle(stroke_color=GREEN_C, stroke_opacity=0.7, fill_color=RED_B, fill_opacity=0.5, height=1, width=1)

        dot = always_redraw(lambda: Dot().move_to(box.get_center()))

        code = Code("Tute4Code1.py", style=Code.styles_list[12], background="window", language="python",
                    insert_line_no=True,
                    tab_width=2, line_spacing=0.3, font="Monospace").set_width(6).to_edge(UL, buff=0)

        self.play(FadeIn(plane), Write(code), run_time=6)
        self.wait()
        self.add(box, dot)
        self.play(box.animate.shift(RIGHT * 2), run_time=4)
        self.wait()
        self.play(box.animate.shift(UP * 3), run_time=4)
        self.wait()
        self.play(box.animate.shift(DOWN * 5 + LEFT * 5), run_time=4)
        self.wait()
        self.play(box.animate.shift(UP * 1.5 + RIGHT * 1), run_time=4)
        self.wait()


class Tute2(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-7, 7, 1], y_range=[-4, 4, 1]).add_coordinates()

        axes = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1], x_length=6, y_length=6)
        axes.to_edge(LEFT, buff=0.5)

        circle = Circle(stroke_width=6, stroke_color=YELLOW, fill_color=RED_C, fill_opacity=0.8)
        circle.set_width(2).to_edge(DR, buff=0)

        triangle = Triangle(stroke_color=ORANGE, stroke_width=10,
                            fill_color=GREY).set_height(2).shift(DOWN * 3 + RIGHT * 3)

        code = Code("Tute4Code1.py", style=Code.styles_list[12], background="window", language="python",
                    insert_line_no=True,
                    tab_width=2, line_spacing=0.3, font="Monospace").set_width(8).to_edge(UR, buff=0)

        self.play(FadeIn(plane), Write(code), run_time=6)
        self.wait()
        self.play(Write(axes))
        self.wait()
        self.play(plane.animate.set_opacity(0.4))
        self.wait()
        self.play(DrawBorderThenFill(circle))
        self.wait()
        self.play(circle.animate.set_width(1))
        self.wait()
        self.play(Transform(circle, triangle), run_time=3)
        self.wait()


class Tute3(Scene):
    def construct(self):
        rectangle = RoundedRectangle(stroke_width=8, stroke_color=WHITE,
                                     fill_color=BLUE_B, width=4.5, height=2).shift(UP * 3 + LEFT * 4)

        mathtext = MathTex("\\frac{3}{4} = 0.75"
                           ).set_color_by_gradient(GREEN, PINK).set_height(1.5)
        mathtext.move_to(rectangle.get_center())
        mathtext.add_updater(lambda x: x.move_to(rectangle.get_center()))

        code = Code("Tute4Code1.py", style=Code.styles_list[12], background="window", language="python",
                    insert_line_no=True, font_size=12,
                    tab_width=2, line_spacing=0.3, font="Monospace").set_width(8).to_edge(UR, buff=0)

        self.play(Write(code), run_time=6)
        self.wait()

        self.play(FadeIn(rectangle))
        self.wait()
        self.play(Write(mathtext), run_time=2)
        self.wait()

        self.play(rectangle.animate.shift(RIGHT * 1.5 + DOWN * 5), run_time=6)
        self.wait()
        mathtext.clear_updaters()
        self.play(rectangle.animate.shift(LEFT * 2 + UP * 1), run_time=6)
        self.wait()


class Tute4(Scene):
    def construct(self):
        r = ValueTracker(0.5)  # Tracks the value of the radius

        circle = always_redraw(lambda:
                               Circle(radius=r.get_value(), stroke_color=YELLOW,
                                      stroke_width=5))

        line_radius = always_redraw(lambda:
                                    Line(start=circle.get_center(), end=circle.get_bottom(), stroke_color=RED_B,
                                         stroke_width=10)
                                    )

        line_circumference = always_redraw(lambda:
                                           Line(stroke_color=YELLOW, stroke_width=5
                                                ).set_length(2 * r.get_value() * PI).next_to(circle, DOWN, buff=0.2)
                                           )

        triangle = always_redraw(lambda:
                                 Polygon(circle.get_top(), circle.get_left(), circle.get_right(), fill_color=GREEN_C)
                                 )

        self.play(LaggedStart(
            Create(circle), DrawBorderThenFill(line_radius), DrawBorderThenFill(triangle),
            run_time=4, lag_ratio=0.75
        ))
        self.play(ReplacementTransform(circle.copy(), line_circumference), run_time=2)
        self.play(r.animate.set_value(2), run_time=5)


class testing(Scene):
    def construct(self):

        play_icon = VGroup(*[SVGMobject(f"{HOME2}\\youtube_icon.svg") for k in range(8)]
                           ).set_height(0.75).arrange(DOWN, buff=0.2).to_edge(UL, buff=0.1)

        time = ValueTracker(0)
        l = 3
        g = 10
        w = np.sqrt(g / l)
        T = 2 * PI / w
        theta_max = 20 / 180 * PI
        p_x = -2
        p_y = 3
        shift_req = p_x * RIGHT + p_y * UP

        vertical_line = DashedLine(start=shift_req, end=shift_req + 3 * DOWN)

        theta = DecimalNumber().move_to(RIGHT * 10)
        theta.add_updater(lambda m: m.set_value((theta_max) * np.sin(w * time.get_value())))

        def get_ball(x, y):
            dot = Dot(fill_color=BLUE, fill_opacity=1).move_to(x * RIGHT + y * UP).scale(3)
            return dot

        ball = always_redraw(lambda:
                             get_ball(shift_req + l * np.sin(theta.get_value()),
                                      shift_req - l * np.cos(theta.get_value()))
                             )

        def get_string():
            line = Line(color=GREY, start=shift_req, end=ball.get_center())
            return line

        string = always_redraw(lambda: get_string())

        def get_angle(theta):
            if theta != 0:
                if theta > 0:
                    angle = Angle(line1=string, line2=vertical_line, other_angle=True, radius=0.5, color=YELLOW)
                else:
                    angle = VectorizedPoint()
            else:
                angle = VectorizedPoint()
            return angle

        angle = always_redraw(lambda: get_angle(theta.get_value()))

        guest_name = Tex("Manoj Dhakal").next_to(vertical_line.get_start(), RIGHT, buff=0.5)
        guest_logo = ImageMobject(f"{HOME}\\guest_logo.png").set_width(2).next_to(guest_name, DOWN, buff=0.1)

        pendulum = Group(string, ball, vertical_line, guest_name, guest_logo)

        self.play(DrawBorderThenFill(play_icon), run_time=3)

        self.add(vertical_line, theta, ball, string, angle)
        self.wait()
        self.play(FadeIn(guest_name), FadeIn(guest_logo))
        self.play(time.animate.set_value(2 * T), rate_func=linear, run_time=2 * T)
        self.play(pendulum.animate.set_height(0.6).move_to(play_icon[7].get_center()), run_time=2)
        self.remove(theta, angle, ball, string)

        self.wait()


class parametric(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes().add_coordinates()
        end = ValueTracker(-4.9)

        graph = always_redraw(lambda:
                              ParametricFunction(lambda u: np.array([4 * np.cos(u), 4 * np.sin(u), 0.5 * u]),
                                                 color=BLUE, t_min=-3 * TAU, t_range=[-5, end.get_value()])
                              )

        line = always_redraw(lambda:
                             Line(start=ORIGIN, end=graph.get_end(), color=BLUE).add_tip()
                             )

        self.set_camera_orientation(phi=70 * DEGREES, theta=-30 * DEGREES)
        self.add(axes, graph, line)
        self.play(end.animate.set_value(5), run_time=3)
        self.wait()


class Test(Scene):
    def construct(self):
        self.camera.background_color = "#FFDE59"

        text = Tex("$3x \cdot 5x = 135$", color=BLACK).scale(1.4)
        text2 = MathTex("15x^2=135", color=BLACK).scale(1.4)
        a = [-2, 0, 0]
        b = [2, 0, 0]
        c = [0, 2 * np.sqrt(3), 0]
        p = [0.37, 1.4, 0]
        dota = Dot(a, radius=0.06, color=BLACK)
        dotb = Dot(b, radius=0.06, color=BLACK)
        dotc = Dot(c, radius=0.06, color=BLACK)
        dotp = Dot(p, radius=0.06, color=BLACK)
        lineap = Line(dota.get_center(), dotp.get_center()).set_color(BLACK)
        linebp = Line(dotb.get_center(), dotp.get_center()).set_color(BLACK)
        linecp = Line(dotc.get_center(), dotp.get_center()).set_color(BLACK)
        equilateral = Polygon(a, b, c)
        triangle = Polygon(a, b, p)
        self.play(Write(equilateral))
        self.wait()
        self.play(Write(VGroup(lineap, linebp, linecp, triangle)))
        self.wait()
        self.play(triangle.animate.rotate(0.4))
        self.wait()

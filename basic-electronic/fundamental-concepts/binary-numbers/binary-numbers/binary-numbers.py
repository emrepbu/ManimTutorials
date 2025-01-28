from manim import *

class BinaryNumberExplanation(Scene):
    def construct(self):
        # Başlık
        title = Text("İkili Sayı Sisteminin Matematiksel Temeli", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        formula_part0 = MathTex(r"N_{10} =", font_size=48, color=BLUE).next_to(title, DOWN * 2 + LEFT * 4)
        formula_part1 = MathTex(r"d_{n-1} \times 2^{n-1} +", font_size=48, color=GREEN).next_to(formula_part0, RIGHT)
        formula_part2 = MathTex(r"d_{n-2} \times 2^{n-2} + ", font_size=48, color=YELLOW).next_to(formula_part1, RIGHT)
        formula_part3 = MathTex(r"\dots + d_0 \times 2^0", font_size=48, color=RED).next_to(formula_part2, RIGHT)

        self.play(Write(formula_part0))
        self.wait(0.5)
        self.play(Write(formula_part1))
        self.wait(0.5)
        self.play(Write(formula_part2))
        self.wait(0.5)
        self.play(Write(formula_part3))
        self.wait(1)

        term1 = MathTex(r"d_{n-1} \times 2^{n-1}", color=GREEN, font_size=42).next_to(formula_part0, DOWN * 2 + RIGHT)
        term1_text = Text("En yüksek basamağın katkısı", font_size=30, color=GREEN).next_to(term1, RIGHT)

        self.play(Indicate(formula_part1))
        self.play(Write(term1), Write(term1_text))
        self.wait(2)

        term2 = MathTex(r"d_{n-2} \times 2^{n-2}", color=YELLOW, font_size=42).next_to(term1, DOWN)
        term2_text = Text("Bir alt basamağın katkısı", font_size=30, color=YELLOW).next_to(term2, RIGHT)

        self.play(Indicate(formula_part2))
        self.play(Write(term2), Write(term2_text))
        self.wait(2)

        term3 = MathTex(r"\dots + d_0 \times 2^0", color=RED, font_size=42).next_to(term2, DOWN)
        term3_text = Text("En düşük basamağın katkısı", font_size=30, color=RED).next_to(term3, RIGHT)

        self.play(Indicate(formula_part3))
        self.play(Write(term3), Write(term3_text))
        self.wait(2)

        self.play(FadeOut(*self.mobjects[1:]))

        example_title = Text(r"Örnek: İkili Sayı 1101_{2}", font_size=30, color=YELLOW).next_to(formula_part0, DOWN, aligned_edge=LEFT)
        self.play(Write(example_title))
        self.wait(1)

        example_step1 = MathTex(
            r"1101_{2} = 1 \times 2^3 + 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0",
            font_size=40
        ).next_to(example_title, DOWN, aligned_edge=LEFT)
        self.play(Write(example_step1))
        self.wait(1)

        example_step2 = MathTex(
            r"1101_{2} = 8 + 4 + 0 + 1",
            font_size=40
        ).next_to(example_step1, DOWN, aligned_edge=LEFT)
        self.play(Transform(example_step1.copy(), example_step2))
        self.wait(1)

        example_step3 = MathTex(
            r"1101_{2} = 13_{10}",
            font_size=50,
            color=ORANGE
        ).next_to(example_step2, DOWN, aligned_edge=LEFT)
        self.play(Transform(example_step2.copy(), example_step3))
        self.wait(2)

        self.play(example_step3.animate.shift(RIGHT).scale(1.5))
        self.wait(2)

        self.play(FadeOut(*self.mobjects))

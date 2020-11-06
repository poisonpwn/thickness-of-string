
from manim import *  # noqa: F403


class IntroExplain(Scene):
    def construct(self):

        # intro String initialisation
        Intro = Tex(
            '\\emph{Formula for finding thickness of thread: }',
            '\\emph{(Indirectly)}')

        In_g = VGroup(Intro[0], Intro[1]).arrange(DOWN, buff=SMALL_BUFF)

        self.play(FadeInFromDown(Intro), run_time=2)
        self.wait()

        Intro.generate_target()  # Intro target
        Intro.target.to_edge(UP)
        Intro.target.scale(0.9)

        self.play(MoveToTarget(Intro), run_time=2)

        # COIL SVG START

        # Create Coil SVG Object
        coil = SVGMobject(
            '/Users/Adhu/Desktop/Scripts/python/Animations/'
            'Thickness_of_string/media/designs/svg_images/Coil.svg')
        coil.scale(1.4)

        coil_text = Tex(
            'String Wrapped around a cylinder', 'i.e a coil').scale(0.75)

        coil_text_vg = VGroup(coil_text[0], coil_text[1]).arrange(
            DOWN, buff=SMALL_BUFF).next_to(coil, DOWN, buff=0.5)

        self.play(Write(coil), FadeInFromDown(coil_text_vg))
        self.wait(3)

        coil.generate_target()
        coil.target.to_edge(RIGHT, buff=2.4)

        self.play(MoveToTarget(coil), FadeOutAndShift(
            coil_text_vg, direction=DOWN))

        # COIL SVG END

        # BRACES START

        coil_bD = Brace(coil, DOWN, buff=SMALL_BUFF)
        coil_bD.scale(0.2)
        coil_bD.shift(RIGHT * 0.75)
        thickness = Tex(
            '\\emph{thickness}', '\\emph{of}', '\\emph{string}')
        thickness.scale(0.8)
        thickness_vg = VGroup(*thickness).arrange(DOWN, SMALL_BUFF)
        thickness_vg.next_to(coil_bD, DOWN, buff=SMALL_BUFF)

        coil_bR = Brace(coil, RIGHT, buff=SMALL_BUFF)
        no_of_turns = Tex('\\emph{no of}', '\\emph{turns}').scale(0.8)
        no_of_turns_vg = VGroup(*no_of_turns).arrange(DOWN, SMALL_BUFF)
        no_of_turns_vg.next_to(coil_bR, RIGHT, buff=SMALL_BUFF)

        coil_bL = Brace(coil, LEFT, buff=SMALL_BUFF)
        length = Tex(
            '\\emph{length}', '\\emph{of}', '\\emph{coil}').scale(0.8)
        length_of_coil_vg = VGroup(*length).arrange(DOWN, buff=SMALL_BUFF)
        length_of_coil_vg.next_to(coil_bL, LEFT, buff=SMALL_BUFF)

        # BRACES END

        self.play(ShowCreation(coil_bR), ShowCreation(
            coil_bL), ShowCreation(coil_bD))
        self.play(Write(no_of_turns_vg), Write(
            length_of_coil_vg), Write(thickness), run_time=1)
        self.wait()

        # FORMULA START

        formula = MathTex('\\emph{Thickness}',
                          '\\emph{of}',
                          '\\emph{string}',
                          '=', '{\\emph{length of coil}',
                          '\\over',
                          '\\emph{no. of turns}}')
        formula.scale(1.1)

        formula.to_edge(LEFT)
        formula[0].shift(UP * 0.4)

        formula[1].next_to(formula[0], DOWN, buff=SMALL_BUFF)
        formula[2].next_to(formula[1], DOWN, buff=SMALL_BUFF)
        formula[3].next_to(formula[1], RIGHT, buff=1)  # 'of' sign
        formula[5].next_to(formula[3], RIGHT, buff=0.5)
        formula[4].next_to(formula[5], UP, buff=SMALL_BUFF)
        formula[6].next_to(formula[5], DOWN, buff=SMALL_BUFF)

        # FORMULA END

        # self.play(*[Write(i) for i in formula])

        # MAIN PLAY

        self.play(ReplacementTransform(thickness[0].copy(), formula[0]),
                  ReplacementTransform(thickness[1].copy(), formula[1]),
                  ReplacementTransform(thickness[2].copy(), formula[2]),
                  FadeInFromDown(formula[3]), run_time=2)
        self.wait()

        self.play(ReplacementTransform(length_of_coil_vg.copy(), formula[4]))
        self.wait()

        self.play(FadeInFrom(formula[5], RIGHT))
        self.wait()

        self.play(ReplacementTransform(no_of_turns_vg.copy(), formula[6]))
        self.wait(2)

        self.play(*[Uncreate(i) for i in [no_of_turns_vg, thickness_vg,
                                          length_of_coil_vg,
                                          coil_bR,
                                          coil_bL,
                                          coil_bD,
                                          In_g, formula, coil]])
        self.wait(4)

        # MAIN PLAY END

        # END SCRIPT

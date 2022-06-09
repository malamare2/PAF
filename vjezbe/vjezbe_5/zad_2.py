import harmonic_oscillator as ho

ho1 = ho.HarmonicOscillator()
ho1.set_initial_conditions(5, 0, 7, 5, 0.01)
ho1.period(2)
ho1.analitickiperiod()
ho1.reset()


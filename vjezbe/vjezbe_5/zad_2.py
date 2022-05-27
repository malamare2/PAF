import harmonic_oscillator as ho

ho1 = ho.HarmonicOscillator()
ho1.set_initial_conditions(3, 0, 5, 15, 0.1, 0.01)
ho1.period(2)
ho1.analitickiperiod()
ho1.reset()

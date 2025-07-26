import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.domain_simulation import make_recording

class TestCase(unittest.TestCase):
    def setUp(self):
        self.record=make_recording(7)

    def test_behavior(self):
        from healthcare_ai.domain_preprocess import clean_signal
        x=self.record.amplitude.to_numpy();y=clean_signal(x,100);self.assertEqual(len(x),len(y));self.assertTrue(np.isfinite(y).all())
        with self.assertRaises(ValueError):clean_signal(x,100,60)

if __name__=="__main__":unittest.main()

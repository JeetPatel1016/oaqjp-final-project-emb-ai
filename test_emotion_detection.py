"""
Unit tests for the `emotion_detector` function.
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """
    Tests for the `emotion_detector` function to validate emotion detection in various statements.
    """

    def test_emotion_detection(self):
        """
        Test to match different emotions based on statements.
        """
        cases = [
            {"statement": "I am glad this happened", "emotion": "joy"},
            {"statement": "I am really mad about this", "emotion": "anger"},
            {"statement": "I feel disgusted just hearing about this", "emotion": "disgust"},
            {"statement": "I am so sad about this", "emotion": "sadness"},
            {"statement": "I am really afraid that this will happen", "emotion": "fear"},
        ]

        for case in cases:
            result = emotion_detector(case['statement'])
            self.assertEqual(result['dominant_emotion'], case['emotion'])

# Ensure final newline at the end of the file
if __name__ == '__main__':
    unittest.main()

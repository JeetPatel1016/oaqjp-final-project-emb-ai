from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
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
        
unittest.main()
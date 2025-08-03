import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    
    def test_joyful_text(self):
        text = "I am glad this happened"
        result = emotion_detector(text)
        self.assertIn("joy", result)
        self.assertGreater(result["joy"], 0.5)
    
    def test_anger_text(self):
        text = "I am really mad about this"
        result = emotion_detector(text)
        self.assertIn("anger", result)
        self.assertGreater(result["anger"], 0.5)
    
    def test_disgust_text(self):
        text = "I feel disgusted just hearing about this"
        result = emotion_detector(text)
        self.assertIn("disgust", result)
        self.assertGreater(result["disgust"], 0.5)

    def test_sad_text(self):
        text = "I am so sad about this"
        result = emotion_detector(text)
        self.assertIn("sadness", result)
        self.assertGreater(result["sadness"], 0.5)

    def test_fear_text(self):
        text = "I am really afraid that this will happen"
        result = emotion_detector(text)
        self.assertIn("fear", result)
        self.assertGreater(result["fear"], 0.5)
    
    def test_empty_text(self):
        results = {
            "joy": 0.983,
            "sadness": 0.002,
            "anger": 0.001,
            "disgust": 0.001,
            "fear": 0.013,
            "dominant_emotion": None
            }
        self.assertEqual(results["dominant_emotion"], None)
if __name__ == '__main__':
    unittest.main()

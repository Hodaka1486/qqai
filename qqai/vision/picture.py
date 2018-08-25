from qqai.classes import QQAIClass, QQAIPicClass, QQAIPicRecognitionClass
import time
import json


class SceneR(QQAIPicRecognitionClass):
    """场景识别"""
    api = 'https://api.ai.qq.com/fcgi-bin/vision/vision_scener'

class ObjectR(QQAIPicRecognitionClass):
    """物体识别"""
    api = 'https://api.ai.qq.com/fcgi-bin/vision/vision_objectr'

class Tag(QQAIPicClass):
    """图像标签识别"""
    api = 'https://api.ai.qq.com/fcgi-bin/image/image_tag'

class ImgToText(QQAIClass):
    """看图说话"""
    api = 'https://api.ai.qq.com/fcgi-bin/vision/vision_imgtotext'

    def make_params(self, image_param):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'image': self.get_image(image_param),
                  'session_id': int(time.time())
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, image_param):
        params = self.make_params(image_param)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class Fuzzy(QQAIPicClass):
    """模糊图片检测"""
    api = 'https://api.ai.qq.com/fcgi-bin/image/image_fuzzy'

class Food(QQAIPicClass):
    """美食图片识别"""
    api = 'https://api.ai.qq.com/fcgi-bin/image/image_food'
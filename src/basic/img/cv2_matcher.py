import cv2

from basic.img import ImageMatcher, ImageLike, MatchResultList, cv2_utils
from basic.log_utils import log


class CvImageMatcher(ImageMatcher):

    def __init__(self):
        self.templates = {}

    def load_template(self, template_id: str, template_path: str, x_scale: float = 1, y_scale: float = 1):
        """
        加载需要匹配的模板到内存中 后续使用模板id匹配即可
        :param template_id: 模板id
        :param template_path: 模板路径
        :param x_scale: 读取后缩放比例x
        :param y_scale: 读取后缩放比例y
        :return:
        """
        res = cv2_utils.read_image_with_alpha(template_path)
        if x_scale != 1 or y_scale != 1:
            res = cv2.resize(res, (0, 0), fx=x_scale, fy=y_scale)

        self.templates[template_id] = res

    def convert_template(self, template_image: ImageLike):
        """
        获取对应模板
        :param template_image: 模板
        :return:
        """
        if type(template_image) == str:
            if template_image not in self.templates:
                return None
            return self.templates[template_image]
        else:
            return template_image

    def match_template_by_id(self, source_image: ImageLike, template_image: ImageLike, threshold: float = 0.5,
                             src_x_scale: float = 1, src_y_scale: float = 1,
                             show_result: bool = False) -> MatchResultList:
        """
        在原图中 匹配模板
        :param source_image: 原图
        :param template_image: 模板
        :param threshold: 匹配阈值
        :param src_x_scale: 原图缩放比例x
        :param src_y_scale: 原图缩放比例y
        :param show_result：是否在最后显示结果图片
        :return: 所有匹配结果
        """
        template: cv2.typing.MatLike = self.convert_template(template_image)
        if template is None:
            log.error('未加载模板 %s' % template_image)
            return MatchResultList()
        source: cv2.typing.MatLike = cv2_utils.convert_source(source_image, src_x_scale=src_x_scale, src_y_scale=src_y_scale)
        match_result_list = cv2_utils.match_with_mask(source, template, threshold)

        log.debug('模板[%s]匹配结果 %s', template_image, str(match_result_list))

        if show_result and len(match_result_list) > 0:
            for i in match_result_list:
                cv2.rectangle(source, (i.x, i.y), (i.x + i.w, i.y + i.h), (255, 0, 0), 1)
            cv2.imshow('Result', source)
        return match_result_list

    def match_template_with_rotation(self, source_image: ImageLike, template_image: str, threshold: float = 0.5,
                                     src_x_scale: float = 1, src_y_scale: float = 1,
                                     show_result: bool = False) -> dict:
        """
        在原图中 对模板进行360度旋转匹配。方法耗时较长 注意原图尽量小一点
        :param source_image: 原图
        :param template_image: 模板id
        :param threshold: 匹配阈值
        :param src_x_scale: 原图缩放比例x
        :param src_y_scale: 原图缩放比例y
        :param show_result：是否在最后显示结果图片
        :return: 每个选择角度的匹配结果
        """
        template: cv2.typing.MatLike = self.convert_template(template_image)
        if template is None:
            log.error('未加载模板 %s' % template_image)
            return {}
        source: cv2.typing.MatLike = cv2_utils.convert_source(source_image)

        angle_result = {}
        for i in range(360):
            rt = cv2_utils.image_rotate(template, i)
            result: MatchResultList = cv2_utils.match_with_mask(source, rt, threshold)
            if len(result) > 0:
                angle_result[i] = result

        return angle_result

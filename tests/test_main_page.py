import pytest
import allure
from data import Answers


class TestMainPage:
    @allure.title('Тест "вопрос-ответ"')
    @pytest.mark.parametrize('question, answer',
                             [(0, Answers.ANSWER_0),
                              (1, Answers.ANSWER_1),
                              (2, Answers.ANSWER_2),
                              (3, Answers.ANSWER_3),
                              (4, Answers.ANSWER_4),
                              (5, Answers.ANSWER_5),
                              (6, Answers.ANSWER_6),
                              (7, Answers.ANSWER_7)])
    def test_questions_and_answer(self, main_page, question, answer):
        main_page.click_on_cookie()
        main_page.scroll_page_to_last_question()
        result = main_page.click_to_question_get_answer(question)
        assert result == answer
import pytest
import allure

from data_collection import QUESTIONS_DATA
from urls import BASE_URL


class TestQuestions:
    @allure.title("Проверка ответа на вопрос: {question}")
    @pytest.mark.parametrize("num", list(QUESTIONS_DATA.keys()))
    def test_question_answer(self, num, main_page):
        question_text, expected_answer = QUESTIONS_DATA[num]
        main_page.go_to_url(BASE_URL)
        actual_answer = main_page.check_question_and_answer(num)
        assert actual_answer == expected_answer, \
            f"Для вопроса '{question_text}' ожидался ответ '{expected_answer}', получен '{actual_answer}'"

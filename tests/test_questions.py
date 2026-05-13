import pytest
import allure
from pages.main_page import MainPage
from data_collection import QUESTIONS_DATA


class TestQuestions:
    @allure.title("Проверка ответа на вопрос: {question}")
    @pytest.mark.parametrize("question, expected_answer", QUESTIONS_DATA)
    def test_question_answer(self, driver, question, expected_answer):
        main_page = MainPage(driver)
        main_page.open()
        answer_text = main_page.get_answer_text(question)
        assert answer_text == expected_answer, (
            f"Ожидался ответ '{expected_answer}', но получен '{answer_text}'"
        )
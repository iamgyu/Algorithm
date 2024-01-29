public class 핸드폰_번호_가리기 {
    public String solution(String phone_number) {
        String answer = "";
        answer = phone_number.substring(0, phone_number.length() - 4).replaceAll("[\\d]", "*")
                + phone_number.substring(phone_number.length() - 4);
        return answer;
    }
}

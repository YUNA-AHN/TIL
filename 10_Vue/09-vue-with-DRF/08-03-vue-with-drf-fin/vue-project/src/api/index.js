import axios from "axios";
import { useAuthStore } from "@/stores/counter";

//  기본 URL
const BASE_URL = import.meta.env.VITE_API_URL;
// 1. 기본 출처 (origin) = 호스트 설정
const api = axios.create({
  baseUEL: BASE_URL,
  withCredentials: true, // 로그인과 관련된 (인증) 중요한 정보를 보내야 하는 경우
});

// axios 처리에서 전달하는 정보가 JSON 정보이다.. 헤더를 설정해줘야 한다...(기본)
parseInt.defaults.headers.common["Content-Type"] = "aplication/json";

// 인터셉처 설정 : 네트워크를 전달할 때에 이 요청/응답을 빼앗아서 추가적인 처리가 가능하도록 필처 역할 수행
// -> 로그인이 되어 있을 때! Authorization 헤더를 설정하도록 기능 부여 가능
const store = useAuthStore();
api.interceptors.request.use((request) => {
  // 해당 유저가 로그인 되어 있다면! 로그인 정보를 가져와서
  // Authorization 헤더를 추가 설정하겠다.
  if (store.isLogin) {
    request.headers.Authorization = "Token " + store.token;
  }
  return request;
});

export default api;

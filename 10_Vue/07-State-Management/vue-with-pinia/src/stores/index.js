import {defineStore} from "pinia"
import {ref}  from "vue"

// 카운터 상태 관리
export const useCounterStore = defineStore(
    "counter", // devTools 식별하기 위한 값으로 첫번째 인자 유니크 값
    () => {
        // states, getters, actions를 정의하고 반환
        const count = ref(0) // 카툰트 변수 states

        // getters == computed
        const doubleCount = computed(() => {
            return count.value * count.value;
          });
        
        // actions ==  함수
        // 증가 함수
        const increment = () => {
            count.value++
        }
        
        // 감소 함수
        const decrement = () => {
            count.value--
        }

        return {
            count,
            increment,
            decrement,
            persist:true // 현 store의 상태값(데이터들을) Local Storage에 저장/복원
        }
    }
)
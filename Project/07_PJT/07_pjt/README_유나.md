# 이현직

# 학습한 내용

- 데이터 상품 목록 정보를 DB에 저장하는 것은 수월하게 진행되었으나,
  옵션 목록 정보를 DB에 저장하는 것이 쉽지 않았다. intr_rate에서 floatfield () 의 상세 조건을 변경하면서 구글링을 해본 결과 null=True, blank=True, default=None 를 조건으로 지정하며 해결할 수 있었다.

# 어려웠던 부분

- 교재를 참고하면서 views.py를 작성하고 runserver를 통해 사이트에 들어간 결과 옵션 목록 정보도 포함되어 나타나게 되었다. depositoptions_set = DepositOptionsSerializer(many=True, read_only=True) 를 주석처리하자 원하는 값이 나타났지만, 필수 조건에 부합하지 않았다.
  따라서 DepositProductsListSerializer serializer를 따로 생성하여 만든 결과 원하는 값이 나타내게 되었다.

# 새로 배운 것들 및 느낀 점

- Postman을 통해 POST를 입력한 결과 처음에 cloud agent error: can not send requests to localhost. select a different agent. 에러가 떠서 Postman's desktop agent를 설치하자 원하는 결과가 나오게 되었다. 또한 중복 입력 값에 대해 처리하는 방법으로는 마지막 return을 'message' : '~' 로 입력하자 원하는 값이 나오게 되었다.

# 안유나

# 학습한 내용

- api를 활용하여 데이터베이스를 구축한 후, rest api를 활용하여 금융상품정보를 제공하는 server를 제작하였습니다.
- api로 받아온 데이터에서 원하는 데이터를 추출하고, 이를 데이터 베이스에 저장하는 것을 배웠습니다.
  - null, blank에 대한 처리
  - 빈 값에 대한 처리
- 원하는 데이터만 출력할 수 있도록 serializer를 설정해주었습니다.

# 어려웠던 부분

- 데이터베이스 구축에서 가장 많은 시간을 투자하였습니다.
  - 처음에는 null과 blank가 존재하는 경우 데이터가 입력되지 않는 오류가 발생하였습니다.  
    이를 해결하기 위하여 default를 지정해주었지만, 해결되지 않았습니다.  
    이후에, null, blank를 True로 설정해주어 데이터 입력에 대한 문제를 해결했습니다.
  - 빈 값에 대한 후속처리에서 어려움을 겪었습니다. 어떤 값으로 받아졌는지 확인하는 것에 어려움 있어 여러가지 시도를 해보았습니다.  
    이후, 값이 존재하지 않으면 -1를 입력해주도록 하여 문제를 해결하였습니다.
- serializer 각각 적용한 후, dict로 반환하는 것을 학습했습니다.

# 새로 배운 것들 및 느낀 점

- 실습실 문제로 연습하던 것과 실제로 데이터를 받아서 구현하는 것에 차이가 있음을 느겼습니다.
- 최대 우대 금리를 추출해주기 위하여 aggregate를 사용해보았습니다
- null, blank에 대한 처리 및 null값에 대한 후속 처리를 새롭게 학습했습니다.
- 초기에 진행했던 프로젝트를 기반으로 새롭게 프로젝트를 진행해보니 싸피의 첫 시작에서 지금까지 얼마나 발전했는지 알 수 있는 시간이었습니다.

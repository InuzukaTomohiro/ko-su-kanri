from sqlalchemy.orm import Session


class TWorkRecords:
    """業務記録のトランザクションの永続処理を行うクラス"""
    
    def __init__(self, session: Session):
        self.session = Session
    
    def set_timer():
        """作業開始時にタイマーをセットするメソッド"""
        
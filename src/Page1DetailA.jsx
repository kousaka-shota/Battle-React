import { useLocation, useHistory } from "react-router-dom";

export const Page1DetailA = () => {
  const { state } = useLocation();
  const history = useHistory();
  const onClickBack = () => history.goBack();
  return (
    <>
      <h1>aaa</h1>;<button onClick={onClickBack}>戻る</button>
    </>
  );
};

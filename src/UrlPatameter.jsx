import { useParams, useLocation } from "react-router-dom";

export const UrlPatameter = () => {
  //urlparamを取得
  const { id } = useParams();
  //querypatameterを取得する方法
  const { search } = useLocation();
  const query = new URLSearchParams(search);

  return (
    <>
      <h1>UrlPatameter</h1>
      <p>{id}</p>
      <p>query {query.get("name")}</p>
    </>
  );
};

import { useLocation } from "react-router-dom";

export const Page1DetailA = () => {
  const { state } = useLocation();
  return;
  <>
    <h1>aaa</h1>;
    {state.map((num) => (
      <p key={num}>{num}</p>
    ))}
  </>;
};

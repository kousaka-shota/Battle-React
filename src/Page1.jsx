import { Link, BrowzerRouter, Switch, Router } from "react-router-dom";

export const Page1 = () => {
  const arr = [...Array(100).keys()];
  return (
    <>
      <h1>Page1</h1>
      <Link to={{ pathname: "/page1/detailA", state: arr }}>A</Link>
      <br />
      <Link to="/page1/detailB">B</Link>
    </>
  );
};

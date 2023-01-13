import { Link, BrowzerRouter, Switch, Router } from "react-router-dom";

export const Page1 = () => {
  return (
    <>
      <h1>Page1</h1>
      <Link to="/page1/detailA">A</Link>
      <br />
      <Link to="/page1/detailB">B</Link>
    </>
  );
};

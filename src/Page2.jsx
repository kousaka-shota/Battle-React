import { Link, BrowzerRouter, Switch, Router } from "react-router-dom";

export const Page2 = () => {
  return (
    <div>
      <h1>Page2</h1>
      <Link to="page2/100">URL parapara</Link>
      <br />
      <Link to="page2/100?name=hogehoge">Query parapara</Link>
    </div>
  );
};

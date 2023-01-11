import { useState } from "react";
import "./styles.css";

export const App = () => {
  const [monsters, setMonsters] = useState([{ name: "a", HP: 10 }]);
  const [name, setName] = useState("");
  const [hp, setHp] = useState("");

  //各要素のセット及び再レンダリング
  const onChangeName = (event) => setName(event.target.value);
  const onChangeHP = (event) => setHp(event.target.value);
  //送信ボタンクリックでモンスター情報をセット
  const onClickSubmit = () => {
    const newMonsters = [...monsters, { name: name, HP: hp }];
    setMonsters(newMonsters);
  };
  return (
    <div>
      <form action="#">
        <p>名前</p>
        <input id="name" type="text" onChange={onChangeName} />
        <p>体力</p>
        <input type="number" onChange={onChangeHP} />
        <p>攻撃力</p>
        <input type="number" />
        <br />
        <input type="submit" onClick={onClickSubmit} />
      </form>
      <div>
        {monsters.map((monster) => {
          return (
            <div key={monster} className="mons">
              <p>名前：{monster.name}</p>
              <p>HP：{monster.HP}</p>
              <button>Attack</button>
            </div>
          );
        })}
      </div>
    </div>
  );
};

import './App.css';
import { useState } from "react";

function App() {
	const title = '개발 Blog';
	
	let [ products, setProducts ] = useState([
		{ title: '파이썬 독학', date: '2021년 2월 19일 발행', like: 0 },
		{ title: '역삼 우동 맛집', date: '2021년 2월 18일 발행', like: 0 },
		{ title: '남자 코트 추천', date: '2021년 2월 17일 발행', like: 0 },
	]);
	
	const onClick = (index) => {
		let newProducts = [ ...products ];
		newProducts[index].like++;
		setProducts(newProducts);
	};
	
	return (
		<div className="App">
			<div className="header">
				<h2>{title}</h2>
			</div>
			
			{products.map((product, index) =>
				<div className="list">
					<h4>{product.title} <span onClick={() => onClick(index)}>👍</span> {product.like}</h4>
					<p>{product.date}</p>
				</div>
			)}
			
			<br/>
			
			<div>
				<button onClick={() => {
					setProducts([ ...products ].sort((a, b) => (a.title).localeCompare(b.title)))
				}}><strong>사전 순으로 정렬하기</strong>
				</button>
			</div>
		</div>
	);
}

export default App;
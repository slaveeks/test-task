import React from 'react';
import Container from './components/layouts/Container';
import Graph from './components/UI/graph/Graph';
import GraphContainer from './components/layouts/GraphContainer';
import OrdersInfoContainer from './components/layouts/OrdersInfoContainer';
import TotalInfo from './components/UI/totalInfo/TotalInfo';
import Table from './components/UI/table/Table';

/**
 * Makes the main page
 *
 * @return {JSX.Element}
 */
function App(): JSX.Element {
  return (
    <Container>
      <GraphContainer>
        <Graph/>
      </GraphContainer>
      <OrdersInfoContainer>
        <TotalInfo/>
        <Table/>
      </OrdersInfoContainer>
    </Container>
  );
}

export default App;

import React from 'react';
import Container from './components/layouts/Container';
import Table from './components/UI/table/Table';
import Graph from './components/UI/graph/Graph';
import GraphContainer from './components/layouts/GraphContainer';
import TotalInfo from './components/UI/totalInfo/TotalInfo';

/**
 * Makes the main page
 *
 * @return {JSX.Element}
 */
function App(): JSX.Element {
  return (
    <Container>
      <Table/>
      <GraphContainer>
        <Graph/>
      </GraphContainer>
      <TotalInfo/>
    </Container>
  );
}

export default App;

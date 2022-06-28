import React from 'react';
import styled from 'styled-components';

/**
 * Interface for graph container component props
 */
interface Props{
}

/**
 * Styled graph container component
 *
 * @param props - props of component
 */
const GraphContainerStyled = styled.div<Props>`
  position: static;
  height: 500px;
  width: 800px;
`;

/**
 * Graph container component
 *
 * @param {Props} props - props of component
 *
 * @return {React.FC<Props>}
 */
const GraphContainer: React.FC<Props> = ({...props}) => {
  return (
    <GraphContainerStyled {...props}/>
  );
};

export default GraphContainer;

import React from 'react';
import styled from 'styled-components';

/**
 * Interface for column component props
 */
interface Props{
  // Cell text
  text: string;
  // Key for map
  key?: number;
}

/**
 * Column component
 *
 * @param {Props} props - props of component
 *
 * @return {React.FC<Props>}
 */
const Column: React.FC<Props> = ({...props}) => {
  return (
    <ColumnStyled {...props}>
      {props.text}
    </ColumnStyled>
  );
};


/**
 * Styled column component
 *
 * @param props - props of component
 */
const ColumnStyled = styled.td<Props>`
  border: 1px solid black;
`;

export default Column;

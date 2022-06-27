import React from 'react';
import styled from 'styled-components';

/**
 * Interface for container component props
 */
interface Props{
  text: string;
  key: string;
}

/**
 * Styled container component
 *
 * @param props - props of component
 */
const ColumnStyled = styled.td<Props>`
  border: 1px solid black;
`;

/**
 * Container component
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

export default Column;

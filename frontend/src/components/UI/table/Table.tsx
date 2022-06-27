import React, {useState, useEffect} from 'react';
import styled from 'styled-components';
import Row from './Row';
import Column from './Column';
import {Transport} from '../../../transport/transport';

/**
 * Interface for container component props
 */
interface Props{
}

/**
 * Styled container component
 *
 * @param props - props of component
 */
const TableStyled = styled.table<Props>`
  width: 800px;
  border: 1px solid black;
  border-collapse: collapse;
`;

/**
 * Container component
 *
 * @param {Props} props - props of component
 *
 * @return {React.FC<Props>}
 */
const Table: React.FC<Props> = ({...props}) => {
  const [data, setData] = useState<Array<Array<string | number>> | null>(null);

  useEffect(() => {
    const exec = async (): Promise<void> => {
      const response = await Transport.getAllData();
      console.log(response);
      setData(response);
    };

    exec();
  }, []);
  return (
    <TableStyled {...props}>
      <Row isArticleRow={true} key={'1'}>
        <Column text={'№'} key={'1'}/>
        <Column text={'заказ №'} key={'1'}/>
        <Column text={'стоимость,$'} key={'1'}/>
        <Column text={'срок поставки'} key={'1'}/>
        <Column text={'стоимость,₽'} key={'1'}/>
      </Row>
      { data ? data!.map((entity) =>
        <Row isArticleRow={false} key={'1'}>
          {entity.map((a) =>
            <Column text={a.toString()} key={'1'}/>,
          )}
        </Row>,
      ): null}
    </TableStyled>
  );
};

export default Table;
